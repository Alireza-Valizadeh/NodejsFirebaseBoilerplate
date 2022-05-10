import * as admin from "firebase-admin";
import constants from "./constants";

const otherApp = admin.initializeApp(
  {
    databaseURL: constants.other_DB_URL,
  },
  "otherApp"
);

const otherDB = otherApp.database();

export default otherDB;
