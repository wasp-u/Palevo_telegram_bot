async def scan(self, scan_id, data):
    if data['lock'].locked():
        return

    async with data['lock']:
        data['attempts'] += 1

        train = await self.client.fetch_train(
            data['date'], data['source'], data['destination'], data['train_num'])
        if train is None:
            return self.handle_error(
                scan_id, data, 'Train {} not found'.format(data['train_num']))

        if data['ct_letter']:
            coach_type = self.find_coach_type(train, data['ct_letter'])
            if coach_type is None:
                return self.handle_error(
                    scan_id, data, 'Coach type {} not found'.format(data['ct_letter']))
            coach_types = [coach_type]
        else:
            coach_types = train.coach_types

        session_id = await self.book(train, coach_types, data['firstname'], data['lastname'])
        if session_id is None:
            return self.handle_error(scan_id, data, 'No available seats')

        await self.success_cb(data['success_cb_id'], session_id)
        self.abort(scan_id)

@staticmethod
async def book(train, coach_types, firstname, lastname):
    with UZClient() as client:
        for coach_type in coach_types:
            for coach in await client.list_coaches(train, coach_type):
                try:
                    seats = await client.list_seats(train, coach)
                except ResponseError:
                    continue
                for seat in seats:
                    try:
                        await client.book_seat(train, coach, seat, firstname, lastname)
                    except ResponseError:
                        continue
                    return client.get_session_id()


