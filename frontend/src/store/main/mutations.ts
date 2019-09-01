import { IUserProfile, IUserNotifyStatus, INotifyUser } from '@/interfaces';
import { MainState, AppNotification } from './state';
import { getStoreAccessors } from 'typesafe-vuex';
import { State } from '../state';
import Vue from 'vue';

export const mutations = {
    setToken(state: MainState, payload: string) {
        state.token = payload;
    },
    setLoggedIn(state: MainState, payload: boolean) {
        state.isLoggedIn = payload;
    },
    setLogInError(state: MainState, payload: boolean) {
        state.logInError = payload;
    },
    setUserProfile(state: MainState, payload: IUserProfile) {
        state.userProfile = payload;
    },
    setDashboardMiniDrawer(state: MainState, payload: boolean) {
        state.dashboardMiniDrawer = payload;
    },
    setDashboardShowDrawer(state: MainState, payload: boolean) {
        state.dashboardShowDrawer = payload;
    },
    addNotification(state: MainState, payload: AppNotification) {
        state.notifications.push(payload);
    },
    removeNotification(state: MainState, payload: AppNotification) {
        state.notifications = state.notifications.filter((notification) => notification !== payload);
    },
    setNotify(state: MainState, payload: INotifyUser) {
        const notifies = state.notifies.filter((notifyUser) => notifyUser.id !== payload.id);
        notifies.push(payload);
        state.notifies = notifies;

    },
    setNotifyUpdated(state: MainState, payload: INotifyUser) {
        const notify = state.notifies.filter((notifyUser) => notifyUser.id === payload.id);
        const index = state.notifies.indexOf(notify[0]);
        Vue.set(state.notifies, index, payload);
    },
    setNotifies(state: MainState, payload: INotifyUser[]) {
        state.notifies = payload;
    },
    removeNotify(state: MainState, payload: INotifyUser) {
        state.notifies = state.notifies.filter((notifyUser) => notifyUser.id !== payload.id);
    },
};

const { commit } = getStoreAccessors<MainState | any, State>('');

export const commitSetDashboardMiniDrawer = commit(mutations.setDashboardMiniDrawer);
export const commitSetDashboardShowDrawer = commit(mutations.setDashboardShowDrawer);
export const commitSetLoggedIn = commit(mutations.setLoggedIn);
export const commitSetLogInError = commit(mutations.setLogInError);
export const commitSetToken = commit(mutations.setToken);
export const commitSetUserProfile = commit(mutations.setUserProfile);
export const commitAddNotification = commit(mutations.addNotification);
export const commitRemoveNotification = commit(mutations.removeNotification);

export const commitSetNotify = commit(mutations.setNotify);
export const commitSetNotifyUpdated = commit(mutations.setNotifyUpdated);
export const commitRemoveNotify = commit(mutations.removeNotify);
export const commitSetNotifies = commit(mutations.setNotifies);
