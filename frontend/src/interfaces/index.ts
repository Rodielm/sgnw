export interface IUserProfile {
    email: string;
    isActive: boolean;
    isAdmin: boolean;
    full_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    full_name?: string;
    password?: string;
    isActive?: boolean;
    isAdmin?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    full_name?: string;
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
