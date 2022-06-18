export default function validateUid(uid: string, guid: string): boolean {
  const areIdsIdentical: boolean = uid === guid;
  console.assert(areIdsIdentical, "user IDs do not match");
  if (!uid || !guid) {
    console.log(`Falsy values uid: ${uid} guid ${guid}`);
    return false;
  }
  return areIdsIdentical && uid.length > 20;
}
