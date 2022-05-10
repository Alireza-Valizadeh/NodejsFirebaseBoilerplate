import * as admin from "firebase-admin";
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
