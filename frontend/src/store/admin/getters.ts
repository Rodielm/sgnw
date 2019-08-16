import { AdminState } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';

export const getters = {
    adminUsers: (state: AdminState) => state.users,
    adminOneUser: (state: AdminState) => (userId: number) => {
        const filteredUsers = state.users.filter((user) => user.id === userId);
        if (filteredUsers.length > 0) {
            return { ...filteredUsers[0] };
        }
    },
    adminGroups: (state: AdminState) => state.groups,
    adminOneGroup: (state: AdminState) => (groupId: number) => {
        const filteredGroups = state.groups.filter((group) => group.id === groupId);
        if (filteredGroups.length > 0) {
            return { ...filteredGroups[0] };
        }
    },
    adminRoles: (state: AdminState) => state.roles,
    adminOneRole: (state: AdminState) => (roleId: number) => {
        const filteredRoles = state.roles.filter((role) => role.id === roleId);
        if (filteredRoles.length > 0) {
            return { ...filteredRoles[0] };
        }
    },
    adminApps: (state: AdminState) => state.apps,
    adminOneApp: (state: AdminState) => (appId: number) => {
        const filteredaApps = state.apps.filter((app) => app.id === appId);
        if (filteredaApps.length > 0) {
            return { ...filteredaApps[0] };
        }
    },
};

const { read } = getStoreAccessors<AdminState, State>('');

export const readAdminOneUser = read(getters.adminOneUser);
export const readAdminUsers = read(getters.adminUsers);

export const readAdminApps = read(getters.adminApps);
export const readAdminOneApp = read(getters.adminOneApp);

export const readAdminGroups = read(getters.adminGroups);
export const readAdminOneGroup = read(getters.adminOneGroup);

export const readAdminRoles = read(getters.adminRoles);
export const ReadAdminOneRole = read(getters.adminOneRole);

