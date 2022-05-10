
/** @type {import('ts-jest/dist/types').InitialOptionsTsJest} */
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  testRegex: "/src/__tests__/.*.test.ts",
  testTimeout: 60000
};