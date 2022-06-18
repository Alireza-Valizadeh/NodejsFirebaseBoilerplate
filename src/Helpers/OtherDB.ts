import * as admin from "firebase-admin";
import constants from "./constants";

const backendApp = admin.initializeApp(
  {
    databaseURL: constants.BACKEND_DB_URL,
  },
  "backendApp"
);

const backendDB = backendApp.database();

export default backendDB;
