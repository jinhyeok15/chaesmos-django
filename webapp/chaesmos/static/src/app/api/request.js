import { POST, PUT, GET } from './http.js';
import { HOST } from './config.js';

// requests

export const createSolution = async (body) => {
  return await POST(`${HOST}/api/postoffice/solve/`, body);
}
