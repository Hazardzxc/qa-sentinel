import { test as base, expect } from '@playwright/test';

// Blocks browser requests to any origin outside the env allowlist, e.g. a redirect from DEV to production.
// shortcut: covers browser traffic only; the `request` fixture (API tests) is not routed, so API clients must build URLs from baseURL.
const allowed = new Set<string>(JSON.parse(process.env.QA_ALLOWED_ORIGINS ?? '[]'));

export const test = base.extend({
  context: async ({ context }, use) => {
    await context.route('**/*', (route) => {
      const { origin } = new URL(route.request().url());
      return allowed.has(origin) ? route.fallback() : route.abort('blockedbyclient');
    });
    await use(context);
  },
});

export { expect };
