import { IUserProfile, IGroup, IApp, IRole, ILang } from '@/interfaces';

export interface AdminState {
    users: IUserProfile[];
    groups: IGroup[];
    apps: IApp[];
    roles: IRole[];
    langs:ILang[];
}
