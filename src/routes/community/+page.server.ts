import { BACKEND, GET, COMMUNITY_ENDPOINTS } from '../../lib/constants';
import { fail } from '@sveltejs/kit';
// on page load, check for jwt and redirect if jwt present
// export const load = async (event) => {
//     const jwt = event.cookies.get('jwt')
//     if (!jwt) throw redirect(302, '/login');

//     const response = await GET(BACKEND + COMMUNITY_ENDPOINTS.COMMUNITY_SPONSOR)
//     console.log(response)
//     const form = await superValidate(event, communityCreate);
//     return {
//         form
//     };
// };


// placeholder for what i will do, which is send the GET request, and if it succeeds, allow through, and if not, redirect
export const load = async ({ fetch, cookies }) => {
    const jwt = cookies.get('jwt')
    if (!jwt) throw redirect(302, '/login'); 
    const response = await fetch(BACKEND + COMMUNITY_ENDPOINTS.COMMUNITY_CREATE)
    if (response.status !== 200) {
        var errorObj = {}
        {
            // this is all just a way to parse the html error received. I'm still not certain if I intend to do anything with it or not yet, since a generic error might be all that's needed.
            const reader = response.body?.getReader()
            let reading = true;

            while (reading) {
                const { done, value } = await reader?.read()
                if (done) break
                let val = new TextDecoder().decode(value)
                errorObj[val] = val
            }
            // return error
            console.log(errorObj)
            return { error: errorObj, status:response.status }
        }
    }
    console.log(data)

}
