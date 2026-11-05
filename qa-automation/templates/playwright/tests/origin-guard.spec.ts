import { test, expect } from '../fixtures/origin-guard';

// Self-check of the safety fixture. Uses fake responses only, so it sends no real network traffic.
test('TC-QA-001 origin guard blocks unlisted origins @web @functional @p1', async ({ page, baseURL }) => {
  await page.route(`${baseURL}/**`, (route) => route.fulfill({ contentType: 'text/html', body: '<h1>ok</h1>' }));
  await page.goto('/');
  await expect(page.getByRole('heading', { name: 'ok' })).toBeVisible();

  await expect(page.goto('https://not-allowed.invalid/')).rejects.toThrow(/ERR_BLOCKED_BY_CLIENT/);
});
