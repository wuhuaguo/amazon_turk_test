import boto.mturk.connection

sandbox_host = 'mechanicalturk.sandbox.amazonaws.com'
real_host = 'mechanicalturk.amazonaws.com'

mturk = boto.mturk.connection.MTurkConnection(
    aws_access_key_id = 'AKIAILNUJ4FPTRTIEUOQ',
    aws_secret_access_key = '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',
    host = sandbox_host,
    debug = 1 # debug = 2 prints out all requests. but we'll just keep it at 1
)

print boto.Version
print mturk.get_account_balance()
