"""Report exact-match decisions and critical review failures for toy cases."""
import json
from pathlib import Path
from .policy import propose

FIXTURE = Path(__file__).with_name('fixtures.jsonl')


def evaluate(path=FIXTURE):
    cases = [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line.strip()]
    if not cases:
        raise ValueError('No evaluation cases')
    results = []
    for case in cases:
        actual = propose(case)
        results.append({'id':case['id'], 'expected':case['expected'], 'actual':actual,
                        'pass':actual == case['expected']})
    passing = sum(r['pass'] for r in results)
    return {'total':len(results),'passed':passing,'accuracy':passing/len(results), 'cases':results}


def main():
    report = evaluate()
    print(f"Decision accuracy: {report['passed']}/{report['total']} ({report['accuracy']:.1%})")
    for case in report['cases']:
        print(f"{'PASS' if case['pass'] else 'FAIL'} {case['id']}: expected={case['expected']} actual={case['actual']}")
    print('These are toy case results, not a production safety or LLM quality claim.')


if __name__ == '__main__':
    main()
