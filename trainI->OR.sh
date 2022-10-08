export BS=16;
PYTHONPATH=../../../src
USE_TF=0

python ./run_translation.py \
        --output_dir  ./output \
        --model_name_or_path t5-3b \
        --cache_dir  ./cache \
        --evaluation_strategy epoch \
        --save_strategy epoch \
        --do_train \
        --do_eval \
        --train_file ./FLUTEfinaltrain.json \
        --validation_file ./FLUTEfinalvaljson \
        --overwrite_output_dir \
        --max_source_length 1024 \
        --max_target_length 256 \
        --num_train_epochs 10 \
        --gradient_accumulation_steps 64 \
        --per_device_train_batch_size $BS \
        --per_device_eval_batch_size $BS \
        --source_lang en_XX \
        --target_lang en_XX