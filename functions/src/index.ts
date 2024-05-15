import "./Helpers/defaultApp";
import * as functions from "firebase-functions";
export const HelloWorld = functions.https.onRequest(async(req, res): Promise<any> => {
  return res.send("Hello world!");
});

