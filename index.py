import os
here = os.getcwd()
dir = os.path.join(here, "src")
if not os.path.exists(dir):
    os.mkdir(dir)

dataDir = os.path.join(here, "src", "DataAccess")
if not os.path.exists(dataDir):
    os.mkdir(dataDir)
validatorsDir = os.path.join(here, "src", "Validators")
if not os.path.exists(validatorsDir):
    os.mkdir(validatorsDir)
configsDir = os.path.join(here, "src", "Configs")
if not os.path.exists(configsDir):
    os.mkdir(configsDir)
testsDir = os.path.join(here, "src", "__tests__")
if not os.path.exists(testsDir):
    os.mkdir(testsDir)
helpersDir = os.path.join(here, "src", "Helpers")
if not os.path.exists(helpersDir):
    os.mkdir(helpersDir)
servicesDir = os.path.join(here, "src", "Configs")
if not os.path.exists(servicesDir):
    os.mkdir(servicesDir)
dataDirRead = os.path.join(here, "src", "DataAccess", "Read")
if not os.path.exists(dataDirRead):
    os.mkdir(dataDirRead)
dataDirWrite = os.path.join(here, "src", "DataAccess", "Write")
if not os.path.exists(dataDirWrite):
    os.mkdir(dataDirWrite)
testsFileDir = os.path.join(here, "src", "__tests__", "Files")
if not os.path.exists(testsFileDir):
    os.mkdir(testsFileDir)
testIntegrationDir = os.path.join(here, "src", "__tests__", "Integration")
if not os.path.exists(testIntegrationDir):
    os.mkdir(testIntegrationDir)
testUnitDir = os.path.join(here, "src", "__tests__", "Unit")
if not os.path.exists(testUnitDir):
    os.mkdir(testUnitDir)
constants = open(os.path.join(here, "src", "Helpers", "constants.ts"), "w")
constants.write("""const project_name = `ssrtest`;
export const project_id = `ssrtest-cebd9`;
export default {
  BASE_IMAGE_URL: `https://firebasestorage.googleapis.com/v0/b/${project_id}.appspot.com/o/ModelPics`,
  DATABASE_URL: `https://${project_id}.firebaseio.com/`,
  STORAGE_PATH: `gs://${project_id}.appspot.com`,
  LOOKUP_DB_URL: `https://${project_name}-lookups.firebaseio.com/`,
  BACKEND_DB_URL: `https://${project_name}-backends.firebaseio.com/`,
  INITS_DB_URL: `https://${project_name}-inits.firebaseio.com`,
  LOGS_DB_URL: `https://${project_name}-logs.firebaseio.com`,
  REPORTS_DB_URL: `https://${project_name}-reports.firebaseio.com`,
};""")
constants.close()

file = open("src/index.ts", "w")
file.write("""import * as functions from "firebase-functions";
import * as admin from "firebase-admin";
import constants, { project_id } from "./Helpers/constants";

admin.initializeApp({
  databaseURL: constants.DATABASE_URL,
  storageBucket: constants.STORAGE_PATH,
  projectId: project_id,
});

export const HelloWorld = functions.https.onRequest(async(req, res) => {
  return res.send("Hello world!");
});

""")
file.close()
jestConfig = """
/** @type {import('ts-jest/dist/types').InitialOptionsTsJest} */
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  testRegex: "/src/__tests__/.*.test.ts",
  testTimeout: 60000
};"""

jest = open("src/jest.config.js", "w")
jest.write(jestConfig)
jest.close()


serviceKey = open(os.path.join("src", "__tests__", "Files", "sKey.json"), "w")
serviceKey.write("// INSERT SERVICE ACCOUNT KEY HERE")
serviceKey.close()

integrationSampleTest = open(os.path.join("src", "__tests__", "Integration", "sample.test.ts"), "w")
integrationSampleTest.write("""const project_id = "ssrtest-cebd9";
import * as path from "path";
import * as admin from "firebase-admin";

const _test = require("firebase-functions-test")(
  {
    projectId: project_id,
    databaseURL: `https://${project_id}.firebaseio.com/`,
    storageBucket: `gs://${project_id}.appspot.com`,
  },
  path.resolve("../functions/src/__tests__/Files/sKey.srcon")
);
import * as functions from "../../index";

_test.wrap(functions.HelloWorld);
""")
integrationSampleTest.close()

sampleRead = open(os.path.join("src", "DataAccess", "Read", "getSomething.ts"), "w")
sampleReadContents = """import * as admin from "firebase-admin";
export default async function getSomething(
  p1: string,
  p2: string
): Promise<any> {
  let info: any = null;
  try {
    info = (await admin.database().ref(p1).child(p2).once("value")).val();
  } catch (error) {
    console.error("getDefaultFields error", error);
  }
  return info;
}
"""
sampleRead.write(sampleReadContents)
sampleRead.close()


sampleWrite = open(os.path.join("src", "DataAccess", "Write", "setSomething.ts"), "w")
sampleWriteContents = """import * as admin from "firebase-admin";
export default async function setSomething(
  p1: string,
  p2: string,
  info: any
): Promise<null> {
  try {
    await admin.database().ref(p1).child(p2).set(info);
  } catch (error) {
    console.error("setSomething error", error);
  }
  return null;
}
}
"""
sampleWrite.write(sampleWriteContents)
sampleWrite.close()

otherDB = open(os.path.join("src", "Helpers", "OtherDB.ts"), "w")
otherDBContents = """import * as admin from "firebase-admin";
import constants from "./constants";

const otherApp = admin.initializeApp(
  {
    databaseURL: constants.other_DB_URL,
  },
  "otherApp"
);

const otherDB = otherApp.database();

export default otherDB;
"""
otherDB.write(otherDBContents)
otherDB.close()

validateUidContents = """export default function validateUid(uid: string, guid: string): boolean {
  const areIdsIdentical: boolean = uid === guid;
  console.assert(areIdsIdentical, "user IDs do not match");
  if (!uid || !guid) {
    console.log(`Falsy values uid: ${uid} guid ${guid}`);
    return false;
  }
  return areIdsIdentical && uid.length > 28;
}
"""
validateUid = open(os.path.join("src", "Validators", "ValidateUid.ts"), "w")
validateUid.write(validateUidContents)
validateUid.close()

validateUidTestsContent = """import validateUid from "../../Validators/validateUid";
const testUID: string = "create_user_default_settings_test_uid";
describe("validate uid tests", () => {
  it("should return true with same uids", () => {
    expect(validateUid(testUID, "create_user_default_settings_test_uid")).toBe(
      true
    );
  });
  it("should return false with same uids but less length than 28", () => {
    expect(validateUid("test", "test")).toBe(false);
  });
  it("should return false with different uids and long length", () => {
    expect(
      validateUid(
        "testkaldkasvkdvas;khdvasvd;asd1",
        "test2jabsdlhasdfikasdasldhasvdl"
      )
    ).toBe(false);
  });
  it("should return false with different uids", () => {
    expect(validateUid("test1", "test2")).toBe(false);
  });
  it("should return false with no ids", () => {
    expect(validateUid(testUID, "")).toBe(false);
    expect(validateUid("", testUID)).toBe(false);
    expect(validateUid("", "")).toBe(false);
    expect(validateUid("undefined", "undefined")).toBe(false);
  });
});
"""

validateUidTest = open(os.path.join("src", "__tests__", "Unit", "validateUid.test.ts"), "w")
validateUidTest.write(validateUidTestsContent)
validateUidTest.close()