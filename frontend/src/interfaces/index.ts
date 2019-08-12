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

export interface IGroups {
    name?: string;
    app?: string;
    idGroup?: number;
    idApp?: number;
}
