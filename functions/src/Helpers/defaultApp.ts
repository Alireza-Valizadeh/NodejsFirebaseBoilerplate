import "dotenv/config";
import * as admin from "firebase-admin";
import constants from "./constants";
import * as path from "path";

let data: admin.AppOptions;
if (process.env.MODE === "PRODUCTION") {
  data = {
    databaseURL: constants.DATABASE_URL,
    storageBucket: constants.STORAGE_PATH,
    projectId: constants.project_id,
  };
} else {
  data = {
    databaseURL: constants.DATABASE_URL,
    storageBucket: constants.STORAGE_PATH,
    projectId: constants.project_id,
    credential: admin.credential.cert(path.resolve("./certs_ssrtest.json")),
  };
}

const defaultApp = admin.initializeApp(data);

export default defaultApp;

export const defaultDB = defaultApp.database();
export const defaultStorage = defaultApp.storage().bucket();
