import { IUserProfile, IGroup, IApp, IRole, ILang, IFileUpload } from '@/interfaces';
import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const mutations = {
    setUsers(state: AdminState, payload: IUserProfile[]) {
        state.users = payload;
    },
    setUser(state: AdminState, payload: IUserProfile) {
        const users = state.users.filter((user: IUserProfile) => user.id !== payload.id);
        users.push(payload);
        state.users = users;
    },
    setGroup(state: AdminState, payload: IGroup) {
        const groups = state.groups.filter((group: IGroup) => group.id !== payload.id);
        groups.push(payload);
        state.groups = groups;
    },
    setGroups(state: AdminState, payload: IGroup[]) {
        state.groups = payload;
    },
    setRole(state: AdminState, payload: IRole) {
        const roles = state.roles.filter((role: IRole) => role.id !== payload.id);
        roles.push(payload);
        state.roles = roles;
    },
    setRoles(state: AdminState, payload: IRole[]) {
        state.roles = payload;
    },
    setApp(state: AdminState, payload: IApp) {
        const apps = state.apps.filter((app: IApp) => app.id !== payload.id);
        apps.push(payload);
        state.apps = apps;
    },
    setApps(state: AdminState, payload: IApp[]) {
        state.apps = payload;
    },
    setLang(state: AdminState, payload: ILang) {
        const langs = state.langs.filter((lang: ILang) => lang.id !== payload.id);
        langs.push(payload);
        state.langs = langs;
    },
    setLangs(state: AdminState, payload: ILang[]) {
        state.langs = payload;
    },
    addFile(state: AdminState, payload: IFileUpload) {
        state.files.push(payload);
    },
    removeUser(state: AdminState, payload: IUserProfile) {
        state.users = state.users.filter((user) => user.id !== payload.id);
    },
    removeGroup(state: AdminState, payload: IGroup) {
        state.groups = state.groups.filter((group) => group.id !== payload.id);
    },
    removeRole(state: AdminState, payload: IRole) {
        state.roles = state.roles.filter((role) => role.id !== payload.id);
    },
    removeApp(state: AdminState, payload: IApp) {
        state.apps = state.apps.filter((app) => app.id !== payload.id);
    },
    removeLang(state: AdminState, payload: ILang) {
        state.langs = state.langs.filter((lang) => lang.id !== payload.id);
    },
    removeFile(state: AdminState, payload: IFileUpload) {
        state.files = state.files.filter((file) => file !== payload);
    },
    removeAllFile(state: AdminState) {
        state.files = [];
    },

};

const { commit } = getStoreAccessors<AdminState, State>('');

export const commitSetUser = commit(mutations.setUser);
export const commitSetUsers = commit(mutations.setUsers);

export const commitSetGroup = commit(mutations.setGroup);
export const commitSetGroups = commit(mutations.setGroups);

export const commitSetRole = commit(mutations.setRole);
export const commitSetRoles = commit(mutations.setRoles);

export const commitSetApp = commit(mutations.setApp);
export const commitSetApps = commit(mutations.setApps);

export const commitSetLang = commit(mutations.setLang);
export const commitSetLangs = commit(mutations.setLangs);

export const commitAddFile = commit(mutations.addFile);
export const commitRemoveFile = commit(mutations.removeFile);

export const commitRemoveAllFile = commit(mutations.removeAllFile);

export const commitRemoveUser = commit(mutations.removeUser);
export const commitRemoveGroup = commit(mutations.removeGroup);
export const commitRemoveRole = commit(mutations.removeRole);
export const commitRemoveApp = commit(mutations.removeApp);
export const commitRemoveLang = commit(mutations.removeLang);
