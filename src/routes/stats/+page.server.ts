import { STAT_ENDPOINTS, GET } from '$lib/constants';
// import type { PageServerLoad } from './$types'

// fetch stats on page load
export const load = async () => {
    const data = await GET(STAT_ENDPOINTS.STATS + "?tag=starsoffseason6&username=mori")
    console.log(data);
    return {data: data}

}