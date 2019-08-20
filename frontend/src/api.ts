import axios from 'axios';
import { apiUrl } from '@/env';
import {
  IUserProfile,
  IUserProfileUpdate,
  IUserProfileCreate,
  IGroup,
  IGroupCreate,
  IGroupUpdate,
  IApp,
  IRole,
  IRoleUpdate,
  IRoleCreate,
  IAppCreate,
  IAppUpdate,
  ILangCreate,
  ILangUpdate,
  ILang,
} from './interfaces';

function authHeaders(token: string) {
  return {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  };
}

export const api = {
  async logInGetToken(username: string, password: string) {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    return axios.post(`${apiUrl}/api/v1/login/access-token`, params);
  },
  async getMe(token: string) {
    return axios.get<IUserProfile>(`${apiUrl}/api/v1/users/me`, authHeaders(token));
  },
  async updateMe(token: string, data: IUserProfileUpdate) {
    return axios.put<IUserProfile>(`${apiUrl}/api/v1/users/me`, data, authHeaders(token));
  },
  async getUsers(token: string) {
    return axios.get<IUserProfile[]>(`${apiUrl}/api/v1/users/`, authHeaders(token));
  },
  async getGroups(token: string) {
    return axios.get<IGroup[]>(`${apiUrl}/api/v1/groups/`, authHeaders(token));
  },
  async getRoles(token: string) {
    return axios.get<IRole[]>(`${apiUrl}/api/v1/roles/`, authHeaders(token));
  },
  async getApps(token: string) {
    return axios.get<IApp[]>(`${apiUrl}/api/v1/apps/`, authHeaders(token));
  },
  async getLangs(token: string) {
    return axios.get<ILang[]>(`${apiUrl}/api/v1/langs/`, authHeaders(token));
  },
  async updateUser(token: string, userId: number, data: IUserProfileUpdate) {
    return axios.put(`${apiUrl}/api/v1/users/${userId}`, data, authHeaders(token));
  },
  async updateGroup(token: string, groupId: number, data: IGroupUpdate) {
    return axios.put(`${apiUrl}/api/v1/groups/${groupId}`, data, authHeaders(token));
  },
  async updateRole(token: string, roleId: number, data: IRoleUpdate) {
    return axios.put(`${apiUrl}/api/v1/roles/${roleId}`, data, authHeaders(token));
  },
  async updateApp(token: string, appId: number, data: IAppUpdate) {
    return axios.put(`${apiUrl}/api/v1/apps/${appId}`, data, authHeaders(token));
  },
  async updateLang(token: string, langId: number, data: ILangUpdate) {
    return axios.put(`${apiUrl}/api/v1/lang/${langId}`, data, authHeaders(token));
  },
  async createUser(token: string, data: IUserProfileCreate) {
    return axios.post(`${apiUrl}/api/v1/users/`, data, authHeaders(token));
  },
  async createGroup(token: string, data: IGroupCreate) {
    return axios.post(`${apiUrl}/api/v1/groups/`, data, authHeaders(token));
  },
  async createRole(token: string, data: IRoleCreate) {
    return axios.post(`${apiUrl}/api/v1/roles/`, data, authHeaders(token));
  },
  async createApp(token: string, data: IAppCreate) {
    return axios.post(`${apiUrl}/api/v1/apps/`, data, authHeaders(token));
  },
  async createLang(token: string, data: ILangCreate) {
    return axios.post(`${apiUrl}/api/v1/lang/`, data, authHeaders(token));
  },
  async passwordRecovery(email: string) {
    return axios.post(`${apiUrl}/api/v1/password-recovery/${email}`);
  },
  async resetPassword(password: string, token: string) {
    return axios.post(`${apiUrl}/api/v1/reset-password/`, {
      new_password: password,
      token,
    });
  },
};
