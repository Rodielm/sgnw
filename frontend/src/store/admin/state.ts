import { IUserProfile, IGroup, IApp, IRole, ILang, IFileUpload } from '@/interfaces';

export interface AdminState {
    users: IUserProfile[];
    groups: IGroup[];
    apps: IApp[];
    roles: IRole[];
    langs: ILang[];
    files: IFileUpload[];
}
