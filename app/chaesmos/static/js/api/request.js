import { LOCALHOST, POST, PUT, GET } from './http.js';

export const HOST = LOCALHOST;

// uri
export const LOGOUT_URI = () => '/api/user/logout/';

// requests

export const requestLogout = async () => {
  return await POST(`${HOST}${LOGOUT_URI()}`);
}
