let project_id;
let project_name;
if (process.env.MODE === "PRODUCTION") {
  project_name = `glo3d`;
  project_id = `glo3d-c338b`;
} else {
  project_name = `ssrtest`;
  project_id = `ssrtest-cebd9`;
}

export default {
  BASE_IMAGE_URL: `https://firebasestorage.googleapis.com/v0/b/${project_id}.appspot.com/o/ModelPics`,
  DATABASE_URL: `https://${project_id}.firebaseio.com/`,
  STORAGE_PATH: `gs://${project_id}.appspot.com`,
  LOOKUP_DB_URL: `https://${project_name}-lookups.firebaseio.com/`,
  BACKEND_DB_URL: `https://${project_name}-backends.firebaseio.com/`,
  MARKET_DB_URL: `https://${project_name}-marketplaces.firebaseio.com/`,
  ANALYTICS_DB_URL: `https://${project_name}-analytics.firebaseio.com/`,
  INITS_DB_URL: `https://${project_name}-inits.firebaseio.com`,
  LOGS_DB_URL: `https://${project_name}-logs.firebaseio.com`,
  REPORTS_DB_URL: `https://${project_name}-reports.firebaseio.com`,
  project_id: project_id,
};
