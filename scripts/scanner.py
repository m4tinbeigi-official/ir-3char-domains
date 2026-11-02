import httpx, concurrent.futures, json, time

client = httpx.Client(
    verify=False,
    timeout=5.0,
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
)

def check(d):
    for attempt in range(2):
        try:
            r = client.get(f'https://whois.nic.ir/WHOIS?name={d}')
            t = r.text.lower()
            if 'error:101' in t or 'no entries found' in t:
                return d, 'FREE'
            elif 'domain:' in t:
                return d, 'TAKEN'
        except Exception:
            time.sleep(0.3)
    return d, 'UNKNOWN'

candidates = [
    # QA (Quality Assurance / Q&A)
    'qa1.ir', 'qa2.ir', 'qa3.ir', 'qa4.ir', 'qa5.ir', 'qa6.ir', 'qa7.ir', 'qa8.ir', 'qa9.ir',
    '1qa.ir', '2qa.ir', '3qa.ir', '4qa.ir', '5qa.ir', '6qa.ir', '7qa.ir', '8qa.ir', '9qa.ir',
    # ML
    '1ml.ir', '2ml.ir', '3ml.ir', '4ml.ir', '5ml.ir', '6ml.ir', '7ml.ir', '8ml.ir', '9ml.ir',
    # PB (Publish / Public)
    'pb1.ir', 'pb2.ir', 'pb3.ir', 'pb4.ir', 'pb5.ir', 'pb6.ir', 'pb7.ir', 'pb8.ir', 'pb9.ir',
    '1pb.ir', '2pb.ir', '3pb.ir', '4pb.ir', '5pb.ir', '6pb.ir', '7pb.ir', '8pb.ir', '9pb.ir',
    # BK (Book)
    '1bk.ir', '2bk.ir', '3bk.ir', '4bk.ir', '5bk.ir', '6bk.ir', '7bk.ir', '8bk.ir', '9bk.ir',
    # RD (Read)
    '1rd.ir', '2rd.ir', '3rd.ir', '4rd.ir', '6rd.ir', '8rd.ir',
    # TX (Text)
    '1tx.ir', '2tx.ir', '3tx.ir', '4tx.ir', '5tx.ir', '6tx.ir',
    # WR (Write)
    '1wr.ir', '6wr.ir',
    # CV (Cover)
    'cv1.ir', 'cv2.ir', 'cv3.ir', 'cv5.ir', 'cv6.ir', 'cv7.ir', 'cv8.ir', 'cv9.ir',
    '1cv.ir', '2cv.ir', '3cv.ir', '4cv.ir', '5cv.ir', '6cv.ir', '7cv.ir', '8cv.ir', '9cv.ir',
    # LN (Line)
    'ln1.ir', 'ln2.ir', 'ln3.ir', 'ln4.ir', 'ln5.ir', 'ln7.ir', 'ln8.ir', 'ln9.ir',
    '1ln.ir', '2ln.ir', '3ln.ir', '4ln.ir', '5ln.ir', '6ln.ir', '7ln.ir', '8ln.ir', '9ln.ir',
    # NO (Novel)
    'no1.ir', 'no2.ir', 'no3.ir', 'no4.ir', 'no5.ir', 'no6.ir', 'no7.ir', 'no8.ir', 'no9.ir',
    '1no.ir', '2no.ir', '3no.ir', '4no.ir', '5no.ir', '6no.ir', '7no.ir', '8no.ir', '9no.ir',
    # LI (Library)
    'li1.ir', 'li2.ir', 'li3.ir', 'li4.ir', 'li5.ir', 'li6.ir', 'li7.ir', 'li8.ir', 'li9.ir',
    '1li.ir', '2li.ir', '3li.ir', '4li.ir', '5li.ir', '6li.ir', '7li.ir', '8li.ir', '9li.ir',
    # PO (Podcast)
    'po1.ir', 'po2.ir', 'po3.ir', 'po5.ir', 'po6.ir', 'po7.ir', 'po8.ir', 'po9.ir',
    '1po.ir', '2po.ir', '3po.ir', '4po.ir', '5po.ir', '6po.ir', '7po.ir', '8po.ir', '9po.ir',
    # FM (FM Radio)
    'fm1.ir', 'fm2.ir', 'fm3.ir', 'fm4.ir', 'fm5.ir', 'fm6.ir', 'fm8.ir', 'fm9.ir',
    '1fm.ir', '2fm.ir', '3fm.ir', '4fm.ir', '5fm.ir', '6fm.ir', '7fm.ir', '8fm.ir', '9fm.ir',
    # FL (Film / Flutter)
    'fl1.ir', 'fl2.ir', 'fl3.ir', 'fl4.ir', 'fl5.ir', 'fl6.ir', 'fl7.ir', 'fl8.ir', 'fl9.ir',
    '1fl.ir', '2fl.ir', '3fl.ir', '4fl.ir', '5fl.ir', '6fl.ir', '7fl.ir', '8fl.ir', '9fl.ir',
    # VD (Video)
    'vd1.ir', 'vd2.ir', 'vd3.ir', 'vd4.ir', 'vd5.ir', 'vd6.ir', 'vd7.ir', 'vd8.ir', 'vd9.ir',
    '1vd.ir', '2vd.ir', '3vd.ir', '4vd.ir', '5vd.ir', '6vd.ir', '7vd.ir', '8vd.ir', '9vd.ir',
    # MD (Media / Markdown)
    'md1.ir', 'md2.ir', 'md3.ir', 'md4.ir', 'md5.ir', 'md6.ir', 'md7.ir', 'md8.ir', 'md9.ir',
    '1md.ir', '2md.ir', '3md.ir', '4md.ir', '5md.ir', '6md.ir', '7md.ir', '8md.ir', '9md.ir',
    # UI & UX
    'ui1.ir', 'ui2.ir', 'ui3.ir', 'ui4.ir', 'ui5.ir', 'ui6.ir', 'ui7.ir', 'ui8.ir', 'ui9.ir',
    '1ui.ir', '2ui.ir', '3ui.ir', '4ui.ir', '5ui.ir', '6ui.ir', '7ui.ir', '8ui.ir', '9ui.ir',
    '1ux.ir', '2ux.ir', '3ux.ir', '4ux.ir', '5ux.ir', '6ux.ir', '7ux.ir', '8ux.ir', '9ux.ir',
    # AR & VR
    'ar1.ir', 'ar2.ir', 'ar3.ir', 'ar4.ir', 'ar5.ir', 'ar6.ir', 'ar7.ir', 'ar8.ir', 'ar9.ir',
    '1ar.ir', '2ar.ir', '3ar.ir', '4ar.ir', '5ar.ir', '6ar.ir', '7ar.ir', '8ar.ir', '9ar.ir',
    'vr1.ir', 'vr2.ir', 'vr3.ir', 'vr4.ir', 'vr5.ir', 'vr6.ir', 'vr7.ir', 'vr8.ir', 'vr9.ir',
    '1vr.ir', '2vr.ir', '3vr.ir', '4vr.ir', '5vr.ir', '6vr.ir', '7vr.ir', '8vr.ir', '9vr.ir',
]

candidates = list(dict.fromkeys(candidates))
print(f'Starting fast threaded scan of {len(candidates)} candidates...')

free_found = []
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    for domain, status in executor.map(check, candidates):
        if status == 'FREE':
            free_found.append(domain)
            print(f'[FOUND FREE] {domain}')

client.close()

with open('/Users/ricksabchez/workspace/projects/ir-3char-domains/new_free_candidates.json', 'w', encoding='utf-8') as f:
    json.dump(free_found, f, ensure_ascii=False, indent=2)

print(f'\nDone! Total verified FREE: {len(free_found)}')
