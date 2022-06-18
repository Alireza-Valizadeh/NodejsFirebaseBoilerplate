import * as functions from "firebase-functions";
import * as admin from "firebase-admin";
import constants, { project_id } from "./Helpers/constants";

admin.initializeApp({
  databaseURL: constants.DATABASE_URL,
  storageBucket: constants.STORAGE_PATH,
  projectId: project_id,
});

export const HelloWorld = functions.https.onRequest(async(req, res): Promise<any> => {
  return res.send("Hello world!");
});

