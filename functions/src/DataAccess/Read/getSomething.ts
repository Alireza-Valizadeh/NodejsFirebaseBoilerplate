import { defaultDB } from "../../Helpers/defaultApp";
export default async function getSomething(
  p1: string,
  p2: string
): Promise<any> {
  let info: any = null;
  try {
    info = (await defaultDB.ref(p1).child(p2).once("value")).val();
  } catch (error) {
    console.error("getDefaultFields error", error);
  }
  return info;
}
