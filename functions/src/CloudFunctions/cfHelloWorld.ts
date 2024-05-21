import * as functions from "firebase-functions";
export const cfHelloWorld = functions.https.onRequest(
  async (req, res): Promise<any> => {
    return res.send("Hello world!");
  }
);
