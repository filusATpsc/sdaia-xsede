-- {"destinationServicename":"sshd","dpt":"2222","dst":"192.168.2.20","level":"info","msg":"Connection","product":"ssh-auth-logger","spt":"29014","src":"61.  177.172.34","time":"2017-03-29T21:08:40Z"}

-- {"client_version":"SSH-2.0-PuTTY","destinationServicename":"sshd","dpt":"2222","dst":"192.168.2.20","duser":"root","level":"info","msg":"Request with pas sword","password":"maidoumaidou","product":"ssh-auth-logger","server_version":"SSH-2.0-OpenSSH_5.3","spt":"29014","src":"61.177.172.34","time":"2017-03-29T21:08:42Z"}

create table sshauth (
day Date DEFAULT toDate(time),
time DateTime,
src String,
spt UInt16,
dst String,
dpt UInt16,
msg Enum8('Connection'=1, 'Request with password'=2, 'Request with key'=3),
client_version String,
duser String,
password String,
fingerprint String
)
ENGINE = MergeTree(day, (day,src), 8192);

--create materialized view sshauth_top
--ENGINE = MaterializedView
--AS select duser, password, uniq(src) as sources from sshauth group by duser,password order by sources DESC;

