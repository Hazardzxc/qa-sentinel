import { defineConfig, devices } from '@playwright/test';
import { readFileSync } from 'node:fs';
import { join } from 'node:path';

// Fail closed: every run must name an approved environment (standards/environment-safety.md).
const envName = (process.env.TEST_ENV ?? '').trim();
if (!envName) throw new Error('TEST_ENV is required, e.g. TEST_ENV=dev. Refusing to guess a target.');
// Production is denied here on purpose. A prod smoke runner needs its own reviewed config, case-ID allowlist and protected CI job.
if (/^prod(uction)?$/i.test(envName)) throw new Error('TEST_ENV=prod is denied by this config. See standards/environment-safety.md.');

type Env = { baseURL: string; allowedOrigins: string[] };
const envs: Record<string, Env> = JSON.parse(readFileSync(join(__dirname, 'config/environments.json'), 'utf8'));
const env = envs[envName];
if (!env) throw new Error(`TEST_ENV=${envName} is not in config/environments.json (${Object.keys(envs).join(', ')}).`);
const base = new URL(env.baseURL);
if (base.protocol !== 'https:') throw new Error(`${envName}.baseURL must be https: ${env.baseURL}`);
if (!env.allowedOrigins?.includes(base.origin)) throw new Error(`${envName}.allowedOrigins must include ${base.origin}`);
// Read by fixtures/origin-guard.ts in each worker.
process.env.QA_ALLOWED_ORIGINS = JSON.stringify(env.allowedOrigins);

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  reporter: [['list'], ['html', { open: 'never' }], ['junit', { outputFile: 'test-results/junit.xml' }]],
  use: {
    baseURL: env.baseURL,
    trace: 'retain-on-failure',
    screenshot: 'only-on-failure',
  },
  // Add only the browsers your product targets.
  projects: [{ name: 'chromium', use: { ...devices['Desktop Chrome'] } }],
});
