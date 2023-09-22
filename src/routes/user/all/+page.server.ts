import {getAllUsers} from "$lib/helpers/allUsers";
import type {PageServerLoad} from "./$types";
export const load: PageServerLoad = async ({ params, fetch }) => {
    const res = await getAllUsers()
    return {
        users: res,
    }
}