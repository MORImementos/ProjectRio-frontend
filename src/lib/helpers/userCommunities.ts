import {GET, USER_ENDPOINTS} from "$lib/constants";
export async function getUserCommunities(username: string) {
    const response = await GET(USER_ENDPOINTS.USER_COMMUNITY, `?username=${username}`)
    const res = await response;
    return res.communities;
}