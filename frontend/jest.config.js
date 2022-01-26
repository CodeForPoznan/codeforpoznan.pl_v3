module.exports = {
  preset: '@vue/cli-plugin-unit-jest',
  setupFiles: ['<rootDir>/jest/jest.setup.js'],
  testMatch: ['**/?(*.)+(spec).js'],
  collectCoverage: true,
  collectCoverageFrom: ['src/**/*', '!src/assets/**'],
  transformIgnorePatterns: ['/node_modules/(?!(vue-scrollactive)/)']
};
