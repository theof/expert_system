#!/bin/sh

set -e

EXPERT_PATH='./expert_system'
TEST_PATH="$(pwd)/test"

cleanup() {
	rm -f cmd.{err,out}
}

trap cleanup EXIT

expert_test() {
	echo $1
	testcase_path="$TEST_PATH/$1"
	cat "$testcase_path" | $EXPERT_PATH > cmd.out 2> cmd.err || true #ignore exit status
	command diff --suppress-common-lines --minimal cmd.out $testcase_path.out
	command diff --suppress-common-lines --minimal cmd.err $testcase_path.err
}

for file in $(find "$TEST_PATH" -type f -name "*.cmd" | xargs basename -s '.cmd');
do
	expert_test "$file"
done

echo 'All tests passed!'
