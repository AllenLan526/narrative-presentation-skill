#!/usr/bin/env python3
"""Validate the production contract used by zine-anchor-deck."""

import json
import sys
from pathlib import Path


FORMATS = {"html", "pptx", "google-slides", "keynote", "pdf", "video", "other"}
ENGINES = {"gathered", "distilled", "lieflat", "scientific-figure", "native"}
BALANCE_MODES = {"neutral", "intentional-asymmetry"}
GAP_TIERS = {"tight", "regular", "major"}
ANIMATION_FIELDS = {
    "trigger",
    "entrance",
    "emphasis",
    "exit",
    "duration_ms",
    "reduced_motion",
}


def require(condition, message, errors):
    if not condition:
        errors.append(message)


def validate(data):
    errors = []
    decision = data.get("format_decision", {})
    output_format = decision.get("output_format")
    require(output_format in FORMATS, f"output_format must be one of {sorted(FORMATS)}", errors)
    require(decision.get("confirmed") is True, "format_decision.confirmed must be true", errors)

    presentation = data.get("presentation", {})
    for field in ("title", "audience", "purpose", "governing_message"):
        require(bool(presentation.get(field)), f"presentation.{field} is required", errors)

    anchor = data.get("visual_anchor", {})
    for field in ("identity", "geometry", "material", "accent_hue", "continuity_rule"):
        require(bool(anchor.get(field)), f"visual_anchor.{field} is required", errors)

    spacing = data.get("spacing_system", {})
    spacing_fields = (
        "base_unit_px",
        "page_margin_px",
        "tight_gap_px",
        "regular_gap_px",
        "major_gap_px",
        "min_text_image_clearance_px",
        "peer_gap_tolerance_ratio",
    )
    for field in spacing_fields:
        require(isinstance(spacing.get(field), (int, float)),
                f"spacing_system.{field} must be numeric", errors)
    if all(isinstance(spacing.get(field), (int, float)) for field in spacing_fields):
        require(spacing["base_unit_px"] > 0, "spacing_system.base_unit_px must be positive", errors)
        require(spacing["page_margin_px"] >= 48,
                "spacing_system.page_margin_px must be at least 48", errors)
        require(0 < spacing["tight_gap_px"] < spacing["regular_gap_px"] < spacing["major_gap_px"],
                "spacing gaps must satisfy 0 < tight < regular < major", errors)
        require(spacing["min_text_image_clearance_px"] >= 24,
                "spacing_system.min_text_image_clearance_px must be at least 24", errors)
        require(1.0 <= spacing["peer_gap_tolerance_ratio"] <= 1.5,
                "spacing_system.peer_gap_tolerance_ratio must be 1.0..1.5", errors)

    credits = data.get("creator_credits")
    require(isinstance(credits, list) and credits, "creator_credits must be a non-empty list", errors)
    if isinstance(credits, list):
        for index, credit in enumerate(credits):
            require(isinstance(credit, dict), f"creator_credits[{index}] must be an object", errors)
            if not isinstance(credit, dict):
                continue
            for field in ("work", "creator", "usage", "location", "license_or_terms"):
                require(bool(credit.get(field)), f"creator_credits[{index}].{field} is required", errors)

    slides = data.get("slides")
    require(isinstance(slides, list) and slides, "slides must be a non-empty list", errors)
    if not isinstance(slides, list):
        return errors

    motion_required = decision.get("motion_required") is True
    slide_ids = set()
    scene_ids = set()
    engines_used = set()
    previous_layout = None
    layout_run = 0

    for index, slide in enumerate(slides, start=1):
        prefix = f"slides[{index - 1}]"
        slide_id = slide.get("id")
        require(bool(slide_id), f"{prefix}.id is required", errors)
        require(slide_id not in slide_ids, f"duplicate slide id: {slide_id}", errors)
        if slide_id:
            slide_ids.add(slide_id)
        for field in ("title", "role", "layout_family", "anchor_state"):
            require(bool(slide.get(field)), f"{prefix}.{field} is required", errors)

        slide_spacing = slide.get("spacing_contract")
        require(isinstance(slide_spacing, dict), f"{prefix}.spacing_contract is required", errors)
        if isinstance(slide_spacing, dict):
            balance_mode = slide_spacing.get("balance_mode")
            require(balance_mode in BALANCE_MODES,
                    f"{prefix}.spacing_contract.balance_mode must be one of {sorted(BALANCE_MODES)}", errors)
            require(bool(slide_spacing.get("title_reserve")),
                    f"{prefix}.spacing_contract.title_reserve is required", errors)
            clearance = slide_spacing.get("text_image_clearance_px")
            min_clearance = spacing.get("min_text_image_clearance_px", 24)
            require(isinstance(clearance, (int, float)) and clearance >= min_clearance,
                    f"{prefix}.spacing_contract.text_image_clearance_px must be at least {min_clearance}", errors)
            require(slide_spacing.get("peer_gap_tier") in GAP_TIERS,
                    f"{prefix}.spacing_contract.peer_gap_tier must be one of {sorted(GAP_TIERS)}", errors)
            exceptions = slide_spacing.get("spacing_exceptions")
            require(isinstance(exceptions, list),
                    f"{prefix}.spacing_contract.spacing_exceptions must be a list", errors)
            if isinstance(exceptions, list):
                for exception_index, exception in enumerate(exceptions):
                    exception_prefix = f"{prefix}.spacing_contract.spacing_exceptions[{exception_index}]"
                    require(isinstance(exception, dict), f"{exception_prefix} must be an object", errors)
                    if isinstance(exception, dict):
                        require(bool(exception.get("relation")), f"{exception_prefix}.relation is required", errors)
                        require(bool(exception.get("purpose")), f"{exception_prefix}.purpose is required", errors)
                if balance_mode == "intentional-asymmetry":
                    require(bool(exceptions),
                            f"{prefix}.spacing_contract requires an exception for intentional-asymmetry", errors)

        layout = slide.get("layout_family")
        layout_run = layout_run + 1 if layout == previous_layout else 1
        require(layout_run <= 2, f"layout family '{layout}' repeats more than twice consecutively", errors)
        previous_layout = layout

        scenes = slide.get("scenes")
        require(isinstance(scenes, list) and 1 <= len(scenes) <= 3,
                f"{prefix}.scenes must contain 1 to 3 scenes", errors)
        if not isinstance(scenes, list):
            continue

        for scene_index, scene in enumerate(scenes):
            scene_prefix = f"{prefix}.scenes[{scene_index}]"
            scene_id = scene.get("id")
            require(bool(scene_id), f"{scene_prefix}.id is required", errors)
            require(scene_id not in scene_ids, f"duplicate scene id: {scene_id}", errors)
            if scene_id:
                scene_ids.add(scene_id)
                require(not slide_id or scene_id.startswith(f"{slide_id}-"),
                        f"scene id '{scene_id}' should start with '{slide_id}-'", errors)
            require(scene.get("engine") in ENGINES,
                    f"{scene_prefix}.engine must be one of {sorted(ENGINES)}", errors)
            engine = scene.get("engine")
            if engine in ENGINES:
                engines_used.add(engine)
            for field in ("role", "subject", "geometry", "anchor_relationship", "alt_text"):
                require(bool(scene.get(field)), f"{scene_prefix}.{field} is required", errors)

            if engine != "native":
                credit_refs = scene.get("credit_refs")
                require(isinstance(credit_refs, list) and credit_refs,
                        f"{scene_prefix}.credit_refs must be a non-empty list", errors)

            if engine == "lieflat":
                chart = scene.get("chart_contract")
                require(isinstance(chart, dict), f"{scene_prefix}.chart_contract is required", errors)
                if isinstance(chart, dict):
                    for field in ("finding", "system", "template_id", "gallery_file", "card_title", "color_system"):
                        require(bool(chart.get(field)), f"{scene_prefix}.chart_contract.{field} is required", errors)
                    audit = chart.get("candidate_audit")
                    require(isinstance(audit, list) and audit,
                            f"{scene_prefix}.chart_contract.candidate_audit is required", errors)
                    if isinstance(audit, list) and len(audit) < 3:
                        require(bool(chart.get("candidate_shortfall_reason")),
                                f"{scene_prefix}.chart_contract needs 3 candidates or candidate_shortfall_reason", errors)

            if engine == "scientific-figure":
                figure = scene.get("figure_contract")
                require(isinstance(figure, dict), f"{scene_prefix}.figure_contract is required", errors)
                if isinstance(figure, dict):
                    for field in ("finding", "figure_type", "publication_target", "source_data", "source_code"):
                        require(bool(figure.get(field)), f"{scene_prefix}.figure_contract.{field} is required", errors)
                    export_formats = figure.get("export_formats")
                    require(isinstance(export_formats, list) and export_formats,
                            f"{scene_prefix}.figure_contract.export_formats must be a non-empty list", errors)
                    if isinstance(export_formats, list):
                        normalized_formats = {str(item).lower() for item in export_formats}
                        require("svg" in normalized_formats or "pdf" in normalized_formats,
                                f"{scene_prefix}.figure_contract.export_formats must include svg or pdf", errors)

            animation = scene.get("animation")
            if motion_required:
                require(isinstance(animation, dict), f"{scene_prefix}.animation is required", errors)
                if isinstance(animation, dict):
                    missing = ANIMATION_FIELDS - animation.keys()
                    require(not missing, f"{scene_prefix}.animation missing {sorted(missing)}", errors)
                    duration = animation.get("duration_ms")
                    require(isinstance(duration, int) and 0 <= duration <= 5000,
                            f"{scene_prefix}.animation.duration_ms must be 0..5000", errors)

    credits_text = " ".join(
        f"{credit.get('work', '')} {credit.get('creator', '')}"
        for credit in credits if isinstance(credit, dict)
    ).lower() if isinstance(credits, list) else ""
    if {"gathered", "distilled"} & engines_used:
        require("zeejay0" in credits_text, "zine scenes require a Zeejay0 creator credit", errors)
    if "lieflat" in engines_used:
        require("lieflat" in credits_text, "lieflat scenes require a Lieflat Charts credit", errors)
        require("moxt" in credits_text or "larashero3-dotcom" in credits_text,
                "Lieflat Charts credit must name Moxt or larashero3-dotcom", errors)
    if "scientific-figure" in engines_used:
        require("scientific-figure-making" in credits_text,
                "scientific-figure scenes require a scientific-figure-making production credit", errors)

    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_deck_plan.py deck-plan.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Deck plan is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
