import validateUid from "../../Validators/validateUid";
const testUID: string = "create_user_default_settings_test_uid";
describe("validate uid tests", () => {
  it("should return true with same uids", () => {
    expect(validateUid(testUID, "create_user_default_settings_test_uid")).toBe(
      true
    );
  });
  it("should return false with same uids but less length than 28", () => {
    expect(validateUid("test", "test")).toBe(false);
  });
  it("should return false with different uids and long length", () => {
    expect(
      validateUid(
        "testkaldkasvkdvas;khdvasvd;asd1",
        "test2jabsdlhasdfikasdasldhasvdl"
      )
    ).toBe(false);
  });
  it("should return false with different uids", () => {
    expect(validateUid("test1", "test2")).toBe(false);
  });
  it("should return false with no ids", () => {
    expect(validateUid(testUID, "")).toBe(false);
    expect(validateUid("", testUID)).toBe(false);
    expect(validateUid("", "")).toBe(false);
    expect(validateUid("undefined", "undefined")).toBe(false);
  });
});
