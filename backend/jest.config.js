module.exports = {
  globalSetup: "/app/tests/setup.js",
  globalTeardown: "/app/tests/teardown.js",
  collectCoverage: true,
  coverageReporters: ["html", "text-summary"],
  collectCoverageFrom: ["**/*.js"],
  coveragePathIgnorePatterns: [
    "/node_modules/",
    "/app/tests/",
    "/app/report/",
    "/app/jest.config.js",
    "/app/utils/populate.js"
  ],
  coverageDirectory: "/app/report/coverage",
  reporters: [
    "default",
    [
      "jest-html-reporter",
      {
        pageTitle: "Test Report",
        outputPath: "/app/report/test-report.html",
        includeFailureMsg: true,
        includeSuiteFailure: true,
        includeStackTrace: true,
        verbose: true,
      },
    ],
  ],
};
