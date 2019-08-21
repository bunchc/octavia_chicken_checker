from cement import Controller, ex


class LoadBalancer(Controller):
    class Meta:
        label = "lb"
        stacked_type = 'embedded'
        stacked_on = 'base'

    @ex(
        help='list broken load balancers',

        # Specify what bit of data are we looking for
        arguments=[
            ### add '-l', '--lb' to look for orphaned load balancers
            ( [ '-t', '--type' ], {
                'help': 'Specify type of thing to list [lb, amphora]',
                'action': 'store',
                'dest': 'type' } ),
        ],
    )
    def list(self):
        lb = {
            'type' : 'lb',
        }
        if self.app.pargs.type is not None:
            lb['type'] = self.app.pargs.type
        self.app.log.info('Listing orphaned %s' % lb['type'])

        # List out the load balancers
        lbs = self.app.conn.load_balancer.load_balancers()
        self.app.log.info('List us some LBs %s' % lbs)
        pass
