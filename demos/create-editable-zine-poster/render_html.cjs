#!/usr/bin/env node
"use strict";

const path = require("path");
const { pathToFileURL } = require("url");
const { chromium } = require("playwright");

async function main() {
  const demoDir = __dirname;
  const htmlPath = path.join(demoDir, "design-as-layers.html");
  const previewPath = path.join(demoDir, "preview.png");
  const pdfPath = path.join(demoDir, "design-as-layers.pdf");

  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1280, height: 1800 }, deviceScaleFactor: 1 });
    await page.goto(pathToFileURL(htmlPath).href, { waitUntil: "load" });
    await page.evaluate(() => document.fonts.ready);
    const audit = await page.evaluate(() => window.posterAudit());
    if (!audit.ok) throw new Error(`Poster DOM audit failed:\n- ${audit.errors.join("\n- ")}`);

    await page.screenshot({ path: previewPath, fullPage: true });
    await page.pdf({
      path: pdfPath,
      width: "1280px",
      height: "1800px",
      margin: { top: "0", right: "0", bottom: "0", left: "0" },
      printBackground: true,
      preferCSSPageSize: true,
      pageRanges: "1",
    });
    process.stdout.write(`${JSON.stringify(audit)}\n`);
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  process.stderr.write(`${error.stack || error}\n`);
  process.exit(1);
});
