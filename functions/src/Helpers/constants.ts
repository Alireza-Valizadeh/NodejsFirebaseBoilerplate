const project_name = `ssrtest`;
export const project_id = `ssrtest-cebd9`;
export default {
  BASE_IMAGE_URL: `https://firebasestorage.googleapis.com/v0/b/${project_id}.appspot.com/o/ModelPics`,
  DATABASE_URL: `https://${project_id}.firebaseio.com/`,
  STORAGE_PATH: `gs://${project_id}.appspot.com`,
  LOOKUP_DB_URL: `https://${project_name}-lookups.firebaseio.com/`,
  BACKEND_DB_URL: `https://${project_name}-backends.firebaseio.com/`,
  INITS_DB_URL: `https://${project_name}-inits.firebaseio.com`,
  LOGS_DB_URL: `https://${project_name}-logs.firebaseio.com`,
  REPORTS_DB_URL: `https://${project_name}-reports.firebaseio.com`,
  project_id: project_id
};