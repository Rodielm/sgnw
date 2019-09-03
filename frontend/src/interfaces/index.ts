export interface IUserProfile {
    email: string;
    isActive: boolean;
    isAdmin: boolean;
    config: string;
    username: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    username?: string;
    password?: string;
    isActive?: boolean;
    isAdmin?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    username?: string;
    password?: string;
    isActive?: boolean;
    isAdmin?: boolean;
}

export interface IGroup {
    id: number;
    name: string;
    description: string;
    isActive: boolean;
    app: IApp;
}

export interface IGroupCreate {
    name: string;
    description?: string;
    app?: IApp;
}

export interface IGroupUpdate {
    name?: string;
    description?: string;
    app?: IApp;
}

export interface IApp {
    name: string;
    description: string;
    version: string;
    isActive?: boolean;
    id: number;
    appLangs?: IAppLang[];
}

export interface IAppCreate {
    name: string;
    description?: string;
    version?: string;
    appLangs: IAppLang[];
}

export interface IAppUpdate {
    name?: string;
    description?: string;
    version?: string;
    appLangs: IAppLang[];
}

export interface IRole {
    id: number;
    name: string;
    description: string;
    isActive: boolean;
    app: IApp;
}

export interface IRoleCreate {
    name: string;
    description?: string;
    app?: IApp;
}

export interface IRoleUpdate {
    name?: string;
    description?: string;
    app?: IApp;
}

export interface ILang {
    id: number;
    name: string;
    isActive: boolean;
}

export interface ILangCreate {
    name: string;
}

export interface ILangUpdate {
    name?: string;
}

export interface IAppLang {
    lang?: ILang;
    version?: string;
    filename?: string;
}

export interface IFileUpload {
    lang?: ILang;
    version?: string;
    file?: File;
    filename?: string;
}

export interface IUserNotifyStatus {
    name?: string;
}

export interface INotifyUser {
    id: number;
    notification?: INotfication;
    user?: IUserProfile;
    status?: IUserNotifyStatus;
    recipient_user?: boolean;
    recipient_group?: IGroup[];
    recipient_roles?: IRole[];
}

export interface INotfication {
    summary: string;
    summary_args: {};
    body: string;
    body_args: {};
    hints: {};
    app: IAppNotification;
    I10n_vers: string;
    expire_ts: Date;
}

export interface IAppNotification {
    id: number;
    name: string;
}
