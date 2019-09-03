import { api } from '@/api';
import { ActionContext } from 'vuex';
import {
    IUserProfileCreate,
    IUserProfileUpdate,
    IGroupCreate,
    IGroupUpdate,
    IRoleUpdate,
    IRoleCreate,
    IAppCreate,
    IAppUpdate,
    ILangCreate,
    ILangUpdate,
    IFileUpload,
} from '@/interfaces';
import { State } from '../state';
import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import {
    commitSetUsers,
    commitSetUser,
    commitSetGroups,
    commitSetApps,
    commitSetGroup,
    commitSetRole,
    commitSetRoles,
    commitSetApp,
    commitSetLang,
    commitSetLangs,
    commitAddFile,
    commitRemoveFile,
    commitRemoveAllFile,
    commitRemoveUser,
    commitRemoveGroup,
    commitRemoveRole,
    commitRemoveApp,
    commitRemoveLang,
} from './mutations';
import { dispatchCheckApiError } from '../main/actions';
import { commitAddNotification, commitRemoveNotification } from '../main/mutations';

type MainContext = ActionContext<AdminState, State>;

export const actions = {
    async actionGetUsers(context: MainContext) {
        try {
            const response = await api.getUsers(context.rootState.main.token);
            if (response) {
                commitSetUsers(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionGetGroups(context: MainContext) {
        try {
            const response = await api.getGroups(context.rootState.main.token);
            if (response) {
                commitSetGroups(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionGetRoles(context: MainContext) {
        try {
            const response = await api.getRoles(context.rootState.main.token);
            if (response) {
                commitSetRoles(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionGetApp(context: MainContext) {
        try {
            const response = await api.getApps(context.rootState.main.token);
            if (response) {
                commitSetApps(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionGetLang(context: MainContext) {
        try {
            const response = await api.getLangs(context.rootState.main.token);
            if (response) {
                commitSetLangs(context, response.data);
            }
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateUser(context: MainContext, payload: { id: number, user: IUserProfileUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateUser(context.rootState.main.token, payload.id, payload.user),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateUserStatus(context: MainContext, payload: { id: number }) {
        const loadingNotification = { content: '', showProgress: true };
        try {
            const response = (await Promise.all([
                api.updateUserStatus(context.rootState.main.token, payload.id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitRemoveUser(context, response.data);
            commitAddNotification(context, { content: 'User successfully removed', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { color: 'error', content: `Error to delete: ${error}` });
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateGroup(context: MainContext, payload: { id: number, group: IGroupUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateGroup(context.rootState.main.token, payload.id, payload.group),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetGroup(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Group successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateGroupStatus(context: MainContext, payload: { id: number }) {
        const loadingNotification = { content: '', showProgress: true };
        try {
            const response = (await Promise.all([
                api.updateGroupStatus(context.rootState.main.token, payload.id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitRemoveGroup(context, response.data);
            commitAddNotification(context, { content: 'Group successfully removed', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { color: 'error', content: `Error to delete: ${error}` });
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateRole(context: MainContext, payload: { id: number, role: IRoleUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateRole(context.rootState.main.token, payload.id, payload.role),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetRole(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Role successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateRoleStatus(context: MainContext, payload: { id: number }) {
        const loadingNotification = { content: '', showProgress: true };
        try {
            const response = (await Promise.all([
                api.updateRoleStatus(context.rootState.main.token, payload.id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitRemoveRole(context, response.data);
            commitAddNotification(context, { content: 'Role successfully removed', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { color: 'error', content: `Error to delete: ${error}` });
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateApp(context: MainContext, payload: { id: number, app: IAppUpdate }) {
        const loadingNotification = { content: 'saving', showProgress: true };
        try {
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateApp(context.rootState.main.token, payload.id, payload.app),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetApp(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'App successfully updated', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { color: 'error', content: `Error to delete: ${error}` });
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateAppStatus(context: MainContext, payload: { id: number }) {
        const loadingNotification = { content: '', showProgress: true };
        try {
            const response = (await Promise.all([
                api.updateAppStatus(context.rootState.main.token, payload.id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitRemoveApp(context, response.data);
            commitAddNotification(context, { content: 'App successfully removed', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { color: 'error', content: `Error to delete: ${error}` });
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateLang(context: MainContext, payload: { id: number, lang: ILangUpdate }) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.updateLang(context.rootState.main.token, payload.id, payload.lang),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetLang(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Language successfully updated', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionUpdateLangStatus(context: MainContext, payload: { id: number }) {
        const loadingNotification = { content: '', showProgress: true };
        try {
            const response = (await Promise.all([
                api.updateLangStatus(context.rootState.main.token, payload.id),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitRemoveLang(context, response.data);
            commitAddNotification(context, { content: 'Lang successfully removed', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { color: 'error', content: `Error to delete: ${error}` });
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateUser(context: MainContext, payload: IUserProfileCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createUser(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetUser(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'User successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateGroup(context: MainContext, payload: IGroupCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createGroup(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetGroup(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Group successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateRole(context: MainContext, payload: IRoleCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createRole(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetRole(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Role successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateApp(context: MainContext, payload: IAppCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createApp(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetApp(context, response.data);
            commitRemoveAllFile(context); // OJO
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'App successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionCreateLang(context: MainContext, payload: ILangCreate) {
        try {
            const loadingNotification = { content: 'saving', showProgress: true };
            commitAddNotification(context, loadingNotification);
            const response = (await Promise.all([
                api.createLang(context.rootState.main.token, payload),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
            commitSetLang(context, response.data);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'Language successfully created', color: 'success' });
        } catch (error) {
            await dispatchCheckApiError(context, error);
        }
    },
    async actionAddFileLocal(context: MainContext, payload: IFileUpload) {
        const loadingNotification = { content: 'adding', showProgress: true };
        try {
            commitAddNotification(context, loadingNotification);
            commitAddFile(context, payload);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'file successfully added', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { color: 'error', content: 'Error wrong with file' });
        }
    },
    async actionRemoveFileLocal(context: MainContext, payload: IFileUpload) {
        const loadingNotification = { content: 'adding', showProgress: true };
        try {
            commitAddNotification(context, loadingNotification);
            commitRemoveFile(context, payload);
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { content: 'file successfully deleted', color: 'success' });
        } catch (error) {
            commitRemoveNotification(context, loadingNotification);
            commitAddNotification(context, { color: 'error', content: 'Error wrong with file' });
        }
    },
    async actionRemoveAppLang(context: MainContext, payload: { idApp: number, idLang: number, file: IFileUpload }) {
        try {
            const response = (await Promise.all([
                api.deleteAppLang(context.rootState.main.token, payload.idApp, payload.idLang),
                await new Promise((resolve, reject) => setTimeout(() => resolve(), 500)),
            ]))[0];
        } catch (error) {
            commitAddNotification(context, { color: 'error', content: `Error to delete: ${error}` });
            await dispatchCheckApiError(context, error);
        }
    },
};

const { dispatch } = getStoreAccessors<AdminState, State>('');

export const dispatchCreateUser = dispatch(actions.actionCreateUser);
export const dispatchGetUsers = dispatch(actions.actionGetUsers);
export const dispatchUpdateUser = dispatch(actions.actionUpdateUser);

export const dispatchGetGroups = dispatch(actions.actionGetGroups);
export const dispatchCreateGroup = dispatch(actions.actionCreateGroup);
export const dispatchUpdateGroup = dispatch(actions.actionUpdateGroup);

export const dispatchGetRoles = dispatch(actions.actionGetRoles);
export const dispatchCreateRole = dispatch(actions.actionCreateRole);
export const dispatchUpdateRole = dispatch(actions.actionUpdateRole);

export const dispatchGetApps = dispatch(actions.actionGetApp);
export const dispatchCreateApp = dispatch(actions.actionCreateApp);
export const dispatchUpdateApp = dispatch(actions.actionUpdateApp);

export const dispatchGetLangs = dispatch(actions.actionGetLang);
export const dispatchCreateLang = dispatch(actions.actionCreateLang);
export const dispatchUpdateLang = dispatch(actions.actionUpdateLang);

export const dispatchAddFileLocal = dispatch(actions.actionAddFileLocal);
export const dispatchRemoveFileLocal = dispatch(actions.actionRemoveFileLocal);

export const dispatchRemoveAppLangs = dispatch(actions.actionRemoveAppLang);

export const dispatchRemoveUser = dispatch(actions.actionUpdateUserStatus);
export const dispatchRemoveGroup = dispatch(actions.actionUpdateGroupStatus);
export const dispatchRemoveRole = dispatch(actions.actionUpdateRoleStatus);
export const dispatchRemoveLang = dispatch(actions.actionUpdateLangStatus);
export const dispatchRemoveApp = dispatch(actions.actionUpdateAppStatus);


