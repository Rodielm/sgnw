import { IUserProfile, IGroup, IApp, IRole } from '@/interfaces';

export interface AdminState {
    users: IUserProfile[];
    groups: IGroup[];
    apps: IApp[];
    roles: IRole[];
}
