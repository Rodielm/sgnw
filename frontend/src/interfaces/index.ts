export interface IUserProfile {
    email: string;
    isActive: boolean;
    isAdmin: boolean;
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
    id: number;
}

export interface IAppCreate {
    name: string;
    description?: string;
    version?: string;
}

export interface IAppUpdate {
    name?: string;
    description?: string;
    version?: string;
}

export interface IRole {
    id: number;
    name: string;
    description: string;
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
}

export interface ILangCreate{
    name:string;
}

export interface ILangUpdate{
    name?:string;
}