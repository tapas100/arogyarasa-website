import { test, expect } from "@playwright/test";

test("home page loads and shows hero", async ({ page }) => {
  await page.goto("http://localhost:3000");
  await expect(page.locator("text=Arogyarasa")).toBeVisible();
  await expect(page.locator("text=Shop Now")).toBeVisible();
});
