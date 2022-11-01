import generator, { Entity, Response } from 'megalodon'


const BASE_URL: string = 'https://mastadon.social'
const access_token: string = ''

const client = generator('mastodon', BASE_URL, access_token)
client.getHomeTimeline()
  .then((res: Response<Array<Entity.Status>>) => {
    console.log(res.data)
  })