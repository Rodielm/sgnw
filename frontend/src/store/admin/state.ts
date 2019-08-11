import { IUserProfile, IGroups } from '@/interfaces';

export interface AdminState {
    users: IUserProfile[];
    groups: IGroups[];
}
