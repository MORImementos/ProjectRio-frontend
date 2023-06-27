import { redirect } from '@sveltejs/kit';
import { GET, USER_ENDPOINTS } from '../../lib/constants';

export const actions = {
    default: async ({ cookies }) => {
        const jwt = cookies.get('jwt')
        // console.log(jwt)
        if (!jwt) {
            throw redirect(302, '/login')

        }
        const response = await GET(USER_ENDPOINTS.LOGOUT)
        cookies.delete('jwt')
        console.log(cookies.get('jwt'))
        throw redirect(302, '/')
    }
}