import { defaultDB } from "../../Helpers/defaultApp";
export default async function setSomething(
  p1: string,
  p2: string,
  info: any
): Promise<null> {
  try {
    await defaultDB.ref(p1).child(p2).set(info);
  } catch (error) {
    console.error("setSomething error", error);
  }
  return null;
}
