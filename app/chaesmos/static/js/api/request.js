import { LOCALHOST, POST, PUT, GET } from './http.js';

export const HOST = LOCALHOST;

// requests

export const requestLogout = async () => {
  return await POST(`${HOST}/api/user/logout/`);
}
