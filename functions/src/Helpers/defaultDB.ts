import * as admin from "firebase-admin";
import constants from "./constants";

const defaultApp = admin.initializeApp(
  {
    databaseURL: constants.DATABASE_URL,
  },
  "defaultApp"
);

const defaultDB = defaultApp.database();

export default defaultDB;
