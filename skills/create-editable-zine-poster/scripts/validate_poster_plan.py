#!/usr/bin/env python3
"""Validate the structural and editability contract of an editable poster plan."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROUTES = {"generation", "brand-template", "apps-sdk", "modular-vector", "html-vector"}
KINDS = {"text", "shape", "image", "chart", "group", "texture"}
EDITABILITY = {
    "native_text",
    "native_shape",
    "native_chart",
    "native_group",
    "swappable_fill",
    "single_vector",
    "fixed_raster",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def require_object(parent: dict, key: str, errors: list[str]) -> dict:
    value = parent.get(key)
    if not isinstance(value, dict):
        fail(errors, f"{key} must be an object")
        return {}
    return value


def require_text(parent: dict, key: str, prefix: str, errors: list[str]) -> str:
    value = parent.get(key)
    if not isinstance(value, str) or not value.strip():
        fail(errors, f"{prefix}.{key} must be non-empty text")
        return ""
    return value.strip()


def require_number(parent: dict, key: str, prefix: str, errors: list[str]) -> float:
    value = parent.get(key)
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        fail(errors, f"{prefix}.{key} must be a number")
        return 0
    return float(value)


def rectangles_intersect(a: dict, b: dict, padding: float = 0) -> bool:
    return (
        a["x"] - padding < b["x"] + b["w"]
        and a["x"] + a["w"] + padding > b["x"]
        and a["y"] - padding < b["y"] + b["h"]
        and a["y"] + a["h"] + padding > b["y"]
    )


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        plan = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"file not found: {path}"]
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc}"]

    if not isinstance(plan, dict):
        return ["root must be an object"]

    fmt = require_object(plan, "format", errors)
    if fmt.get("platform") not in {"canva", "vector"}:
        fail(errors, "format.platform must be 'canva' or 'vector'")
    if fmt.get("design_type") != "poster":
        fail(errors, "format.design_type must be 'poster'")
    if fmt.get("route") not in ROUTES:
        fail(errors, f"format.route must be one of {sorted(ROUTES)}")
    width = require_number(fmt, "width", "format", errors)
    height = require_number(fmt, "height", "format", errors)
    if width <= 0 or height <= 0:
        fail(errors, "format width and height must be positive")
    if fmt.get("orientation") not in {"portrait", "landscape", "square"}:
        fail(errors, "format.orientation must be portrait, landscape, or square")

    poster = require_object(plan, "poster", errors)
    for key in ("title", "audience", "purpose", "governing_message", "viewer_action"):
        require_text(poster, key, "poster", errors)

    anchor = require_object(plan, "visual_anchor", errors)
    for key in ("identity", "geometry", "material", "accent_hue", "continuity_rule"):
        require_text(anchor, key, "visual_anchor", errors)

    spacing = require_object(plan, "spacing_system", errors)
    tight = require_number(spacing, "tight_gap", "spacing_system", errors)
    regular = require_number(spacing, "regular_gap", "spacing_system", errors)
    major = require_number(spacing, "major_gap", "spacing_system", errors)
    minimum = require_number(spacing, "min_text_image_clearance", "spacing_system", errors)
    ratio = require_number(spacing, "peer_gap_tolerance_ratio", "spacing_system", errors)
    require_number(spacing, "base_unit", "spacing_system", errors)
    require_number(spacing, "page_margin", "spacing_system", errors)
    if not (0 < tight < regular < major):
        fail(errors, "spacing gaps must satisfy 0 < tight_gap < regular_gap < major_gap")
    if minimum < 24:
        fail(errors, "min_text_image_clearance must be at least 24")
    if not 1 <= ratio <= 1.5:
        fail(errors, "peer_gap_tolerance_ratio must be between 1 and 1.5")

    credits = plan.get("creator_credits")
    if not isinstance(credits, list):
        fail(errors, "creator_credits must be an array")
    else:
        for index, credit in enumerate(credits):
            if not isinstance(credit, dict):
                fail(errors, f"creator_credits[{index}] must be an object")
                continue
            for key in ("work", "creator", "usage", "location", "license_or_terms"):
                require_text(credit, key, f"creator_credits[{index}]", errors)

    modules = plan.get("modules")
    if not isinstance(modules, list) or not modules:
        fail(errors, "modules must be a non-empty array")
        modules = []
    ids: set[str] = set()
    validated_modules: list[dict] = []
    for index, module in enumerate(modules):
        prefix = f"modules[{index}]"
        if not isinstance(module, dict):
            fail(errors, f"{prefix} must be an object")
            continue
        module_id = require_text(module, "id", prefix, errors)
        if module_id in ids:
            fail(errors, f"duplicate module id: {module_id}")
        ids.add(module_id)
        require_text(module, "role", prefix, errors)
        require_text(module, "owner_group", prefix, errors)
        require_text(module, "alt_text", prefix, errors)
        require_text(module, "source_note", prefix, errors)
        if module.get("kind") not in KINDS:
            fail(errors, f"{prefix}.kind must be one of {sorted(KINDS)}")
        if module.get("kind") == "text" and module.get("bounds_basis") != "rendered_ink":
            fail(errors, f"{prefix}.bounds_basis must be 'rendered_ink' for text")
        if module.get("editability") not in EDITABILITY:
            fail(errors, f"{prefix}.editability must be one of {sorted(EDITABILITY)}")
        z = module.get("z")
        if not isinstance(z, int) or isinstance(z, bool):
            fail(errors, f"{prefix}.z must be an integer")
        bounds = module.get("bounds")
        if not isinstance(bounds, dict):
            fail(errors, f"{prefix}.bounds must be an object")
            continue
        x = require_number(bounds, "x", f"{prefix}.bounds", errors)
        y = require_number(bounds, "y", f"{prefix}.bounds", errors)
        w = require_number(bounds, "w", f"{prefix}.bounds", errors)
        h = require_number(bounds, "h", f"{prefix}.bounds", errors)
        if w <= 0 or h <= 0:
            fail(errors, f"{prefix}.bounds width and height must be positive")
        if x < 0 or y < 0 or x + w > width or y + h > height:
            fail(errors, f"{prefix}.bounds must stay inside the canvas")
        area_ratio = (w * h) / (width * height) if width > 0 and height > 0 else 0
        if module.get("editability") in {"single_vector", "fixed_raster"} and area_ratio > 0.85:
            fail(errors, f"{prefix} flattens more than 85% of the page")
        normalized = dict(module)
        normalized["bounds"] = {"x": x, "y": y, "w": w, "h": h}
        zones = module.get("collision_zones")
        if zones is not None:
            if not isinstance(zones, list) or not zones:
                fail(errors, f"{prefix}.collision_zones must be a non-empty array when present")
            else:
                normalized_zones = []
                for zone_index, zone in enumerate(zones):
                    zone_prefix = f"{prefix}.collision_zones[{zone_index}]"
                    if not isinstance(zone, dict):
                        fail(errors, f"{zone_prefix} must be an object")
                        continue
                    zx = require_number(zone, "x", zone_prefix, errors)
                    zy = require_number(zone, "y", zone_prefix, errors)
                    zw = require_number(zone, "w", zone_prefix, errors)
                    zh = require_number(zone, "h", zone_prefix, errors)
                    if zw <= 0 or zh <= 0:
                        fail(errors, f"{zone_prefix} width and height must be positive")
                    if zx < 0 or zy < 0 or zx + zw > width or zy + zh > height:
                        fail(errors, f"{zone_prefix} must stay inside the canvas")
                    normalized_zones.append({"x": zx, "y": zy, "w": zw, "h": zh})
                normalized["collision_zones"] = normalized_zones
        validated_modules.append(normalized)

    obstacles = [
        module for module in validated_modules
        if module.get("kind") in {"shape", "image", "chart", "texture"}
        and module.get("collision_exempt") is not True
    ]
    for text_module in (module for module in validated_modules if module.get("kind") == "text"):
        exemptions = text_module.get("collision_exemptions", [])
        if not isinstance(exemptions, list) or any(not isinstance(item, str) for item in exemptions):
            fail(errors, f"module {text_module.get('id')}.collision_exemptions must be an array of module IDs")
            exemptions = []
        for obstacle in obstacles:
            if obstacle.get("id") in exemptions:
                continue
            zones = obstacle.get("collision_zones") or [obstacle["bounds"]]
            if any(rectangles_intersect(text_module["bounds"], zone, minimum) for zone in zones):
                fail(
                    errors,
                    f"text module {text_module.get('id')} violates {minimum:g}px clearance "
                    f"from {obstacle.get('id')}",
                )

    owned_contracts = plan.get("owned_text_shape_contracts", [])
    if not isinstance(owned_contracts, list):
        fail(errors, "owned_text_shape_contracts must be an array")
    else:
        for index, contract in enumerate(owned_contracts):
            prefix = f"owned_text_shape_contracts[{index}]"
            if not isinstance(contract, dict):
                fail(errors, f"{prefix} must be an object")
                continue
            require_text(contract, "id", prefix, errors)
            require_text(contract, "shape_id", prefix, errors)
            text_ids = contract.get("text_ids")
            if not isinstance(text_ids, list) or not text_ids or any(not isinstance(item, str) or not item for item in text_ids):
                fail(errors, f"{prefix}.text_ids must be a non-empty array of IDs")
            shape_rotation = require_number(contract, "shape_rotation_degrees", prefix, errors)
            text_rotation = require_number(contract, "text_rotation_degrees", prefix, errors)
            if abs(shape_rotation - text_rotation) > 0.1:
                fail(errors, f"{prefix} shape and text rotations must match")
            shape_height = require_number(contract, "shape_height", prefix, errors)
            text_height = require_number(contract, "text_stack_height", prefix, errors)
            if shape_height <= 0 or text_height <= 0:
                fail(errors, f"{prefix} heights must be positive")
            elif text_height / shape_height > 0.7:
                fail(errors, f"{prefix} text stack exceeds 70% of shape height")
            padding = contract.get("padding")
            if not isinstance(padding, dict):
                fail(errors, f"{prefix}.padding must be an object")
                continue
            values = {}
            for side in ("left", "right", "top", "bottom"):
                values[side] = require_number(padding, side, f"{prefix}.padding", errors)
                if values[side] < tight:
                    fail(errors, f"{prefix}.padding.{side} must be at least tight_gap ({tight:g})")
            for side_a, side_b in (("left", "right"), ("top", "bottom")):
                smaller = min(values[side_a], values[side_b])
                larger = max(values[side_a], values[side_b])
                if smaller > 0 and larger / smaller > 1.5:
                    fail(errors, f"{prefix} {side_a}/{side_b} padding ratio exceeds 1.5")

    exceptions = plan.get("spacing_exceptions")
    if not isinstance(exceptions, list):
        fail(errors, "spacing_exceptions must be an array")
    else:
        for index, item in enumerate(exceptions):
            if not isinstance(item, dict):
                fail(errors, f"spacing_exceptions[{index}] must be an object")
                continue
            require_text(item, "relation", f"spacing_exceptions[{index}]", errors)
            require_text(item, "purpose", f"spacing_exceptions[{index}]", errors)

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_poster_plan.py poster-plan.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    errors = validate(path)
    if errors:
        print("Poster plan validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Poster plan valid: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
